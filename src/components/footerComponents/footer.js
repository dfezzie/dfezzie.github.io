import React, { Component } from 'react';

class Footer extends Component {
  render() {
    return (
    <footer className="mdl-mini-footer">
    <div className="mdl-mini-footer__left-section">
    </div>
    <div className='mdl-mini-footer__center-section'>
    <div className="mdl-logo" id='footer-contact'>Contact Me</div>
      <ul className="mdl-mini-footer__link-list" id='icon-style'>
        <li><a href="https://github.com/dfezzie/"><i className="fab fa-github"></i></a></li>
        <li><a href="https://www.linkedin.com/in/dominicfezzie/"><i className="fab fa-linkedin-in"></i></a></li>
        <li><a href="mailto:dfezzie@gmail.com"><i className="fas fa-envelope"></i></a></li>
      </ul>
    </div>

    </footer>

    );
  }
}

export default Footer;
