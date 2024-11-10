import React from 'react'
// import HeaderClientAdmin from './components/clientAdmin/Header'
// import MainClientAdmin from './components/clientAdmin/Main'

import HeaderBasicUser from './components/basicUser/Header'
import MainBasicUser from './components/basicUser/Main'

// import './styles/clientAdmin/App.css'
import './styles/basicUser/App.css'

function App() {
  return (
    <div className="App">
      {/* <HeaderClientAdmin />
      <MainClientAdmin /> */}
      <HeaderBasicUser />
      <MainBasicUser />
    </div>
  )
}

export default App