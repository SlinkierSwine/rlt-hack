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
                <p className="textHU">Квест 1</p>
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
                            <p>Государственные закупки(44-ФЗ)</p>
                        </div>
                        <div>
                            <p>Государственные закупки(44-ФЗ)</p>
                        </div>
                        <div>
                            <p>Государственные закупки(44-ФЗ)</p>
                        </div>
                    </div>
                </div>
            </div>
        </Fragment>
    )
}