import React, { Component } from 'react';

class Drawer extends Component {
  render() {
    return (
        <div className="mdl-layout__drawer">
        <span className="mdl-layout-title" id='font-override'>Dominic Fezzie</span>
        <nav className="mdl-navigation">
              <a className="mdl-navigation__link" href="">Home</a>
              <a className="mdl-navigation__link" href="">Professional</a>
              <a className="mdl-navigation__link" href="">Personal</a>
              <a className="mdl-navigation__link" href="https://goo.gl/EgC5WC">Resume</a>
        </nav>
      </div>
    );
  }
}

export default Drawer;
