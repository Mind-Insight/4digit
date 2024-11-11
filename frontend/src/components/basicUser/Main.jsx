import React from "react"
import '../../styles/basicUser/Main.css'
import SublimAppBlock from "./SublimAppBlock"
import PartTeamBlock from "./PartTeamBlock"
import TestAndFileBlock from "./TestAndFileBlock"
import FillingFormBlock from "./FillingFormBlock"
import CompleteGameBlock from "./CompleteGameBlock"

import basketProfessions from '../../images/basketProfessions.png'

function Main() {
    return (
        <div className="Main">
            <div className="Main_title">
                Твой путь в <span className="title_color">будущее</span>  IT
            </div>
            <div className="Main_first_block">
                <SublimAppBlock />
                <PartTeamBlock />
            </div>
            <div className="basketProfessions">
                <img src={basketProfessions} alt="basketProfessions" />
            </div>

            <div className="Main_second_block">
                <div className="second_coloum_blocks">
                    <div className="coloum_left_blocks">
                        <TestAndFileBlock />
                    </div>
                    <div className="coloum_right_blocks">
                        <FillingFormBlock />
                        <CompleteGameBlock />
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Main