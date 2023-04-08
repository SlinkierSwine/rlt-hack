import React from 'react'
import { Navbar } from '../navbar/Navbar'
import './Header.scss'
import headerLogo from '../../image/logo.svg'

export const Header = () => {
    return(
        <div className='header'>

            <div className='logoHeader'><img src={headerLogo}></img></div>

            <div className='search'><form action="" method="get"><input name="" placeholder="поиск" type="search"></input></form></div>

            <Navbar></Navbar>

        </div>
    )
}