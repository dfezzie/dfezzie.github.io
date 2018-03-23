import React, { Component } from 'react';

import Professional from './professional'

import Headshot from '../images/headshot.jpg';


class Bio extends Component {
  render() {
    return (
    <main className = "mdl-layout__content">
        <div className="page-content">
            <div className="mdl-grid">
                <div className="mdl-layout-spacer"></div>
                <img className='mdl-cell mdl-cell--4-col mdl-shadow--1dp' src={Headshot} id='portrait'></img>
                <div className="mdl-layout-spacer"></div>
            </div>
            <div className="mdl-grid">
                <div className="mdl-layout-spacer"></div>
                <div className='mdl-cell mdl-cell--5-col mdl-textfield'>
                    <h2 id='center-align'>
                    Dominic Fezzie
                    </h2>
                    <h3 id='center-align'>
                        Software Engineer
                    </h3>
                </div>
                <div className="mdl-layout-spacer"></div>
            </div>
            <Professional />
        </div>
    </main>
    );
  }
}

export default Bio;
