import React, { Component } from 'react';

class Header extends Component {
  render() {
    return (
        <header className="mdl-layout__header">
            <div className="mdl-layout__header-row">
            <span className="mdl-layout-title" id='font-override'>Dominic Fezzie</span>
            <div className="mdl-layout-spacer"></div>
            <nav className="mdl-navigation mdl-layout--large-screen-only">
                <a className="mdl-navigation__link" href="">Home</a>
                <a className="mdl-navigation__link" href="">Professional</a>
                <a className="mdl-navigation__link" href="">Personal</a>
                <a className="mdl-navigation__link" href="">Resume</a>
            </nav>
            </div>
        </header>
    );
  }
}

export default Header;
