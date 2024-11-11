import React from "react"
import '../../styles/basicUser/PartTeamBlock.css'
// import vectorLeft from '../../images/vector_left.svg'

function PartTeamBlock() {
    return (
        <div className="PartTeam_block">
            <div className="PartTeam_title">
                Стань частью <span className="title_spam">нашей</span> команды и развивайся вместе с нами
            </div>
            {/* <img src={vectorLeft} className="PartTeam_vectorLeft" alt="VectorLeft" /> */}
        </div>
    )
}

export default PartTeamBlock