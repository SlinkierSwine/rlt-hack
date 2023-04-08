import React from 'react'
import './Navbar.scss'
import {NavLink} from 'react-router-dom'

export const Navbar = () => {
    return(
        <nav>
            <ul>
                <li>
                    <NavLink to = '/about'>
                        о нас
                    </NavLink>
                </li>
                <li>
                    <NavLink to = '/catalog'>
                        каталог
                    </NavLink>
                </li>
                <li>
                    <NavLink to = '/registration'>
                        личный кабинет
                    </NavLink>
                </li>
            </ul>
        </nav>
    )
}