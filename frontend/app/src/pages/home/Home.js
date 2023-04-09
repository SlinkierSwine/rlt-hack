import React, { Fragment } from "react";
import './Home.scss'
import {Header} from '../../components/header/Header'
import upArrow from '../../image/upArrow.svg'
import star from '../../image/star.svg'
import left_arrow from '../../image/left_arrow.svg'
import rightArrow from '../../image/right_arrow.svg'
import {NavLink} from 'react-router-dom'

export const Home = () => {
    return(
        <Fragment>
             <Header/>
             <div className="contentHome">
                <div className="calendar">
                    <div className="backCalendar"></div>
                    <div className="hCalendar">Календарь</div>
                    <div className="mounthes">
                        <div className="mounth">
                            <div className="mounthName">Декабрь</div>
                            <div className="days">
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                
                            </div>
                        </div>
                        <div className="mounth">
                            <div className="mounthName">Декабрь</div>
                            <div className="days">
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                
                            </div>
                        </div>
                        <div className="mounth">
                            <div className="mounthName">Декабрь</div>
                            <div className="days">
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                <div className="day"></div>
                                
                            </div>
                        </div>
                    </div>
                </div>
                <div className="persona">
                    <div className="backPersona1"></div>
                    <div className="backPersona2"></div>
                    <div className="personalContent">
                        <div className="nameFoto">
                            <div className="foto"></div>
                            <div className="name">Иван Иванов</div>
                        </div>
                        <div className="rating">
                            <div className="personalRating">
                                <div className="hPersonalRating">Личный рейтинг</div>
                                <div className="upArrow"><img src= {upArrow}></img></div>
                                <div className="personalRatingResult">9999 место</div>
                            </div>
                            <div className="grouplRating">
                                <div className="hGroupRating">Групповой рейтинг</div>
                                <div className="upArrow"><img src= {upArrow}></img></div>
                                <div className="groupRatingResult">9999 место</div>
                            </div>
                            <div className="efficiency">
                                <div className="hEfficiency">Эффективность</div>
                                <div className="upArrow"><img src= {upArrow}></img></div>
                                <div className="efficiencyResult">0.99</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="lessons">
                    <NavLink to='/course'>
                        <div className="lesson">
                            <div className="backLesson"></div>
                            <div className="lessonContent">
                                <div className="hLesson">Введение в продажи</div>
                                <div className="chapter">Глава 1</div>
                                <div className="procent">
                                    <div className="procentNumber">100%</div>
                                    <div className="star"><img src={star}></img></div>
                                </div>
                            </div>
                        </div>
                    </NavLink>
                    <NavLink to='/course'>
                        <div className="lesson">
                            <div className="backLesson"></div>
                            <div className="lessonContent">
                                <div className="hLesson">Введение в продажи</div>
                                <div className="chapter">Глава 1</div>
                                <div className="procent">
                                    <div className="procentNumber">100%</div>
                                    <div className="star"><img src={star}></img></div>
                                </div>
                            </div>
                        </div>
                    </NavLink>
                </div>   
             </div>
             <div className="news">
             <div className="newsBack"></div>
             <div className="hNews">Новости</div>
             <div className="nC">
                <div className="leftArrow"><img src={left_arrow}></img></div>
                    <div className="newsContent">
                        <div className="newContent">             
                            <div className="new">
                                <div className="hNew">Майский ивент в самом разгаре</div>
                            </div>
                        </div>
                    </div>
                    <div className="newsContent">
                        <div className="newContent">             
                            <div className="new">
                                <div className="hNew">Майский ивент в самом разгаре</div>
                            </div>
                        </div>
                    </div>
                    <div className="rightArrow"><img src={rightArrow}></img></div>
                </div>
                
            </div> 
             
        </Fragment>   
    )
}