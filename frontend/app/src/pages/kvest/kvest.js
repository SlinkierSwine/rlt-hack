import React, { Fragment } from "react";
import './kvest.scss'
import {Header} from '../../components/header/Header'
import {NavLink} from 'react-router-dom'

export const Kvest = () => {
    return(
        <Fragment>
            <Header/>
            <div className="kvestContent">
                <p className="textH">Примите правильные выбора для развития бизнеса, чтобы достичь успеха!</p>
                <div className="mid">
                    <div className="inMid1">
                        <h1>Пролог:</h1>
                        <p>
                            Вы начинающий предпрениматель, который хочет заниматься закупками.
                            <br /><br />
                            У вас стоит выбор какой тип закупки произвести. У вас пока что начальное представление об ведении торгов на ЭТП.
                        </p>
                    </div>
                    <div className="inMid2">
                        <div>
                            <p>Выбор 1</p>
                        </div>
                        <div>
                            <p>Выбор 2</p>
                        </div>
                        <div>
                            <p>Выбор 3</p>
                        </div>
                    </div>
                </div>

                <div className="buttons">
                    <a href="../../pages/outcome/outcome.js"><button className="btn">
                        Выбор1 
                    </button></a>

                    <NavLink to='/outcome'><button className="btn">
                        Выбор1 
                    </button></NavLink>

                    <NavLink to='/outcome'><button className="btn">
                        Выбор1 
                    </button></NavLink>

                </div>
            </div>
        </Fragment>
    )
}