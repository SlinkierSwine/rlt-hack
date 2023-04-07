import React, { Fragment } from 'react'
import { AddClass } from '../../hoc/AddClass'
import './Layout.scss'
import { Login } from '../../pages/login/Login'
import {Route, Routes} from 'react-router-dom'




const Layout = () => {
        return(
            <Fragment>
                <Login></Login>
            </Fragment>
        )
}


export default AddClass(Layout, 'layout')