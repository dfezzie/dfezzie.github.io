import React, { Component } from 'react';

// Components
import Header from './components/headerComponents/header'
import Drawer from './components/headerComponents/drawer'
import Footer from './components/footerComponents/footer'
import Bio from './components/bodyComponents/bio'

class App extends Component {
  render() {
    return (
      <div className="mdl-layout mdl-js-layout mdl-layout--fixed-header">
        <Header />
        <Drawer />
        <Bio />
        <Footer />
      </div>
    );
  }
}

export default App;
