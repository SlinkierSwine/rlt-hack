import React, { Fragment } from "react";
import './Course.scss'
import {Header} from '../../components/header/Header'
import Ellipse from '../../image/ellipse.svg'
import icon1 from '../../image/icon1.svg'
import icon2 from '../../image/icon2.svg'
import icon3 from '../../image/icon3.svg'
import icon4 from '../../image/icon4.svg'
import icon5 from '../../image/icon5.svg'
import {TextCourse} from '../../components/textCourse/TextCourse'
import {Answer} from '../../components/answer/Answer'
export const Course = () => {
    return(
        <Fragment>
            
            <Header/>
            <div className="courseBack">
                <div className="courseContent">
                        <div className="leftBlock">
                            <div className="chapter">
                                <div className="chapterNumber">Глава 1.</div>
                                <div className="procent">100%</div>
                            </div>
                            <div className="point">
                                <div className="circle"><img src={Ellipse}></img></div>
                                <div className="pointName">Введение в продажи</div>
                            </div>
                            <div className="point">
                                <div className="circle"><img src={Ellipse}></img></div>
                                <div className="pointName">Введение в продажи</div>
                            </div>            
                        </div>
                        <div className="rightBlock">
                                <div className="topBlock">
                                    <div className="progress">Прогресс: 100%</div>
                                    <div className="icons">
                                        <div className="icon"><img src={icon1}></img></div>
                                        <div className="icon"><img src={icon2}></img></div>
                                        <div className="icon"><img src={icon3}></img></div>
                                        <div className="icon"><img src={icon4}></img></div>
                                        <div className="icon"><img src={icon5}></img></div>
                                    </div>
                                </div>

                                <div className="contentCourse">
                                    <Answer/>
                                </div>
                        </div>
                </div>
            </div>
            
        </Fragment>
    )
}