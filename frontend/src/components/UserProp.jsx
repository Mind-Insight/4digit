import React from "react"
import download from './../images/download.svg'
import arrow from './../images/top_arrow.svg'
import close from './../images/close.svg'
import './../styles/UserProp.css'

function UserProp(props) {

    function OpenResume() {
        window.open('https://docs.google.com/document/d/1Kq8SiQC_eCFgN7KdpNHh62f_burbDtoFgCt0KJ7ktME/edit?usp=sharing', '_blank')
    }

    let MBTIType = 'Ошибка'

    if (props.type[0] === 'E' && props.type[5] === 'A') MBTIType = 'Холерик'
    else if (props.type[0] === 'E' && props.type[5] === 'T') MBTIType = 'Сангвиник'
    else if (props.type[0] === 'I' && props.type[5] === 'A') MBTIType = 'Флегматик'
    else if (props.type[0] === 'I' && props.type[5] === 'T') MBTIType = 'Меланхолик'

    return (
        <div className="UserProp">
            <div className="videoBlock">
                <div className="videoTitleBlock">
                    <h3 className="videoTitle">Видеовизитка</h3>
                    <img src={download} alt="download" className="videoDownload" />
                </div>
                <video autoPlay muted loop src={props.video} className="VideoPlayer"></video>
            </div>

            <div className="UserContent">
                <div className="UserContent-top">
                    <div className="UserSoftHard">
                        <div className="UserProgress">
                            <div className="progress progressSoft" style={{ width: 2.44 * +props.soft }}>{props.soft}%</div>
                            <div className="progress progressHard" style={{ width: 2.44 * +props.hard }}>{props.hard}%</div>
                        </div>

                        <div className="progressInfo">
                            <p className="progressInfoSoft">Soft skills</p>
                            <p className="progressInfoHard">Hard skills</p>
                        </div>
                    </div>

                    <div className="UserType">
                        <h3 className="UserType-title">Тип личности</h3>
                        <div className="UserType-MBTI">{props.type}</div>
                        <div className="UserType-Ocean">{MBTIType}</div>
                    </div>
                </div>

                <div className="UserContent-bottom">
                    <div className="resume-btn" >
                        <p className="resume-text">Резюме</p>
                        <div className="resume-href" onClick={OpenResume}>
                            <img src={arrow} alt="click" className="arrowImg" />
                        </div>
                    </div>

                    <div className="invite">
                        <p className="invite-text">Пригласить на собес.</p>
                        <div className="invite-href" onClick={props.onDelete}>
                            <img src={arrow} alt="click" className="arrowImg" />
                        </div>
                    </div>

                    <div className="closeBlock">
                        <div className="close" onClick={props.onDelete}>
                            <img src={close} alt="close" className="closeImg" />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default UserProp