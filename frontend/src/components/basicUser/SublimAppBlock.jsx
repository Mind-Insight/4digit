import React from "react"
import '../../styles/basicUser/SublimAppBlock.css'

import vectorRight from "../../images/vector_right.svg"

function SublimApp() {
    return (
        <div className="Sublim_block">
            <div className="Sublim_topLine">
                <img src={vectorRight} className="Sublim_vectorRight" alt="VectorRight" />
                <div className="Sublim_button">Подать заявку</div>
            </div>
            <div className="Sublim_desription">Подай заявку<span className="title_description">прямо сейчас</span></div>
        </div>
    )
}

export default SublimApp