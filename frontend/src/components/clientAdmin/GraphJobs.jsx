import React from "react"
import '../../styles/clientAdmin/GraphJobs.css'
import graph from '../../images/graphJobs.svg'
import GraphJob from "./GraphJobSingle"

function GraphJobs() {
    return (
        <div className="graphJob">
            <img src={graph} alt="Graph" className="graph" />
            <div className="jobsLine">
                <GraphJob name="Backend" color='#6179FB' />
                <GraphJob name="Frontend" color='#ECECEC' />
                <GraphJob name="QA" color='#DAFB58' />
                <GraphJob name="UI/UX" color='#212121' />
            </div>
        </div>
    )
}

export default GraphJobs