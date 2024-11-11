import React from "react";
import '../../styles/clientAdmin/GraphJobs.css'

function GraphJobSingle(props) {
    return (
        <div className="GraphJob_single">
            <div className="dotJob" style={{ backgroundColor: props.color }}></div>
            <p className="GraphJob_name">{props.name}</p>
        </div>
    )
}

export default GraphJobSingle