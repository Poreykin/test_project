from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django_fsm import FSMField, transition

class Course(MPTTModel):
    name = models.CharField(max_length=50, unique=True, db_index=True, null=False, blank=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

class Task(models.Model):
    solution = models.TextField(db_index=False, null=False, blank=True)

class TaskStatus(models.Model):
    class STATE:
        PROCESS = 'PRC'
        REVIEW = 'RVW'
        DEBT = 'DBT'
        COMPLETE = 'CMP'

    CHOICES = ((STATE.PROCESS, 'process'), (STATE.REVIEW, 'review'), (STATE.DEBT, 'debt'), (STATE.COMPLETE, 'complete'))

    student = models.ForeignKey(User, db_index=True, null=False, blank=False, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, unique=True, db_index=False, null=False, blank=False, on_delete=models.CASCADE)
    state = FSMField(default=STATE.PROCESS, choices=CHOICES, protected=True)

    comment = models.TextField(db_index=False, null=True, blank=True)
    response = models.TextField(db_index=False, null=True, blank=True)

    @transition(field=state, source=[STATE.PROCESS, STATE.DEBT], target=STATE.REVIEW, permission=lambda instance, user: user.pk == instance.student.pk)
    def send(self):
        pass

    @transition(field=state, source=STATE.REVIEW, target=STATE.DEBT, permission=lambda instance, user: user.is_superuser)
    def send_back(self):
        pass

    @transition(field=state, source=STATE.REVIEW, target=STATE.COMPLETE, permission=lambda instance, user: user.is_superuser)
    def accept(self):
        pass
