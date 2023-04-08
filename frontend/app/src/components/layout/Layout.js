import React, { Fragment } from 'react'
import { AddClass } from '../../hoc/AddClass'
import './Layout.scss'
import { Login } from '../../pages/login/Login'
import {Route, Routes} from 'react-router-dom'
import { Home } from '../../pages/home/Home'
import { About } from '../../pages/about/About'
import { Catalog } from '../../pages/catalog/Catalog'
import { PersonalArea } from '../../pages/personalArea/PersonalArea'





const Layout = () => {
        return(
            <Fragment>
                <div className='content'>
                    <div className='routes'>
                    <Routes>
                            <Route path = '/' exact element= {<Home/>}/>
                            <Route path = '/login' exact  element = {<Login/>}/>
                            <Route path = '/about' exact  element = {<About/>}/>
                            <Route path = '/catalog' exact  element = {<Catalog/>}/>
                            <Route path = '/personalArea' exact  element = {<PersonalArea/>}/>
                    </Routes>
                    </div>
                </div>
            </Fragment>
        )
}


export default AddClass(Layout, 'layout')