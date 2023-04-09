import React, { Fragment } from "react";
import './Catalog.scss'
import {Header} from '../../components/header/Header'
import star from '../../image/star.svg'
import {NavLink} from 'react-router-dom'

export const Catalog = () => {
    return(
        <Fragment>
            <Header/>
            <div className="catalogContent">
                <h1>Ежедневные квесты</h1>
            <div className="lessons">
                    <NavLink>
                        <div className="lesson">
                            <div className="backLesson"></div>
                            <div className="lessonContent">
                                <div className="hLesson">Квесты</div>
                                <div className="chapter">Правильный выбор</div>
                            </div>
                        </div>
                    </NavLink>
                    <NavLink>
                        <div className="lesson">
                            <div className="backLesson"></div>
                            <div className="lessonContent">
                                <div className="hLesson">Квесты</div>
                                <div className="chapter">Правильный выбор</div>
                            </div>
                        </div>
                    </NavLink>
                </div>  
            </div>
        </Fragment>
    )
}