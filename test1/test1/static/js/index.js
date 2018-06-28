import React from 'react'
import ReactDOM from 'react-dom'

function Welcome(props) {
  return <b>{props.text}</b>;
}

const element = <Welcome text="window.article" />;

ReactDOM.render(
  element,
  document.getElementById('react')
);
