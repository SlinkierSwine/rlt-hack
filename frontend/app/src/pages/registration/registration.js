import React from "react";
import './registration.scss'
import leftDecor from '../../image/leftDecor.svg'
import rightDecor from '../../image/rightDecor.svg'
import Logo from '../../image/logoLogin.svg'


export const Registration = () => {
    return(
        <div className="backgroundColor">
            <div className="backgroundImage">
                <div className="leftImage"></div>
                <div className="rightImage"></div>
                <div className="hLogin">
                    <img src={Logo}></img>
                </div>
                <div className="loginContent">
                    <div className="logContent">
                            <input placeholder="ФИО" className="login" type="text"></input>
                    </div>
                    <div className="mailContent">
                            <input placeholder="почта" className="mail" type="text"></input>
                    </div>
                    <div className="numberContent">
                            <input placeholder="телефон" className="number" type="text"></input>
                    </div>
                    <div className="passContent">
                            <input placeholder="пароль" className="password" type="password"></input>
                    </div>
                    <div className="repeatPassContent">
                            <input placeholder="повторите пароль" className="repeatPassword" type="password"></input>
                    </div>
                    <div className="sighIn">
                        <button className="but">РЕГИСТРАЦИЯ</button>
                    </div>
                </div>
            </div>

        </div>
    )
}