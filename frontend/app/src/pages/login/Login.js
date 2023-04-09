import React from "react";
import './Login.scss'
import leftDecor from '../../image/leftDecor.svg'
import rightDecor from '../../image/rightDecor.svg'


export const Login = () => {
    return(
        <div className="backgroundColor">
            <div className="backgroundImage">
                <div className="leftImage"></div>
                <div className="rightImage"></div>
                <h1 className="hLogin">RLT.HACK</h1>
                <div className="loginContent">
                    <div className="logContent">
                            <input placeholder="ФИО" className="login" type="text"></input>
                    </div>
                    <div className="passContent">
                            <input placeholder="пароль" className="password" type="password"></input>
                    </div>
                    <div className="forgotRemember">
                        <div className="remember">
                            <input className="checkbox" type="radio" id = "remember_me" name="remember_me"></input>
                            <label for = "remember_me" className="rememberLabel" >Запомни меня</label>
                        </div>
                        <div className="forgot">
                            <a href="#" className="forgotPassword">Забыли пароль?</a>
                        </div>
                    </div>
                    <div className="sighIn">
                        <button className="but">Войти</button>
                    </div>
                    <div className="sighUp">
                        <p className="p"> Нет аккаунта? <span><a href="#" className="sighUpBut">Зарегистрируйтесь</a></span></p>
                    </div>
                </div>
            </div>

        </div>
    )
}