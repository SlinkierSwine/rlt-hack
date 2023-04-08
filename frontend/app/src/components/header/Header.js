import React from 'react'
import { Navbar } from '../navbar/Navbar'
import './Header.scss'
import headerLogo from '../../image/logo.svg'
import {NavLink} from 'react-router-dom'

export const Header = () => {
    return(
        <div className='header'>

            <NavLink to = '/'><div className='logoHeader'><img src={headerLogo}></img></div></NavLink>

            <div className='search'><form action="" method="get"><input name="" placeholder="поиск" type="search"></input></form></div>

            <Navbar></Navbar>

        </div>
    )
}