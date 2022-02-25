import "./App.css"
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Header from './components/Header'
import Footer from './components/Footer'

import HomeScreen from './screens/HomeScreen'
import LoginScreen from './screens/LoginScreen'
import RegisterScreen from './screens/RegisterScreen'
import {useEffect} from "react";


function App() {
    useEffect(
        () => {
            document.title = "WDYFT";
        }, []
    )
    return (
        <BrowserRouter>
            <Header/>
            <br/>
            <main>
                <Routes>
                    <Route path={'/'} element={<HomeScreen/>}/>
                    <Route path={'/login'} element={<LoginScreen/>}/>
                    <Route path={'/register'} element={<RegisterScreen/>}/>
                </Routes>
            </main>
            <Footer/>
        </BrowserRouter>
    );
}

export default App;
