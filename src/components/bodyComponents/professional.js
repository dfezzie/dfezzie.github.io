import React, { Component } from 'react';

class Professional extends Component {
  render() {
    return (
        <div className="page-content">
            <div className="mdl-grid">
                <div className="mdl-layout-spacer"></div>
                <div className='mdl-cell mdl-cell--4-co mdl-js-textfield' id='bio-text'>
                    I am a recent graduate of Florida State University, with a BS in Computer Science. 
                    Currently living in Tampa, working as a Software Engineer for Nielsen. I am always looking for the next opportunity to build something incredible.
                    Feel free to contact me any way you feel fit!
                </div>
                <div className="mdl-layout-spacer"></div>
            </div>
        </div>

    );
  }
}

export default Professional;
