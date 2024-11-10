import React from "react"
import '../../styles/basicUser/TestAndFileBlock.css'
import arrowUpRight from '../../images/arrow_up_right.svg'
import ellipseBlack from '../../images/ellipse_black.svg'
import ellipseGray from '../../images/ellipse_gray.svg'
import cloud from '../../images/cloud.svg'

function TestAndFileBlock() {
    return (
        <div className="TestAndFile_block">
            <div className="Test_block">
                <div className="Test_title">
                    Как Вас зовут?
                </div>
                <div className="review_line">
                    <div className="title_line">ФИО</div>
                    <div className="button_line">
                        <div className="title_button">
                            Далее
                        </div>
                        <img src={arrowUpRight} className="arrowUpRight" alt="arrowUpRight" />
                    </div>
                </div>
                <div className="stage_line">
                    <img src={ellipseBlack} className="ellipseBlack" alt="ellipseBlack" />
                    <img src={ellipseGray} className="ellipseGray" alt="ellipseGray" />
                    <img src={ellipseGray} className="ellipseGray" alt="ellipseGray" />
                    <img src={ellipseGray} className="ellipseGray" alt="ellipseGray" />
                </div>
            </div>

            <div className="File_block">
                <img src={cloud} className="cloud" alt="cloud" />
                <div className="selectFile">
                    Выбрать файл
                </div>
                <div className="fileDescription">
                    Формата MP4, не длиннее <br />1 мин. и не больше 5 мб
                </div>
            </div>
        </div>
    )
}

export default TestAndFileBlock