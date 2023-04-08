import React from "react";
import './Answer.scss';
import LeftArrow from '../../image/left.svg'
import RightArrow from '../../image/right.svg'

export const Answer = () => {
    return(
    <div className="contentDiv">
        <div className="answerH">Задача с развернутым ответом</div>
        <div className="taskText">Какова основаная задача , которую преследует бизнес</div>
        <div className="textField">
            <form>
                <input type="text" className="textAnswer">
                    
                </input>
            </form>
        </div>
        <button className="sent">Отправить</button>
        <div className="arrows">
            <button className="leftArrow">
                <img src={LeftArrow}></img>
            </button>
            <button className="rightArrow">
                <img src={RightArrow}></img>
            </button>
        </div>
        
    </div>
    )
}