import React from "react"
import '../../styles/clientAdmin/Users.css'
import titlePhoto from '../../images/title_photo.svg'
import User from "./User"
import userPhoto from '../../images/profile.png'

function Users() {
    return (
        <div className="Users">
            <h2 className="Users_title">Заявки</h2>
            <div className="title_table">
                <img src={titlePhoto} alt="table_photo" className="table_photo" />
                <p className="table_title table_name">Имя</p>
                <p className="table_title table_phone">Телефон</p>
                <p className="table_title table_email">Email</p>
                <p className="table_title table_soft">Совместимость</p>
            </div>
            <User photo={userPhoto} name='Игнатюк Александр' age='18 лет' phone='+79215435242' email=' odvdplvdplv@gmail.com' soft='87' />
            <User photo={userPhoto} name='Игнатюк Александр' age='18 лет' phone='+79215435242' email=' odvdplvdplv@gmail.com' soft='87' />
            <User photo={userPhoto} name='Игнатюк Александр' age='18 лет' phone='+79215435242' email=' odvdplvdplv@gmail.com' soft='87' />
            <User photo={userPhoto} name='Игнатюк Александр' age='18 лет' phone='+79215435242' email=' odvdplvdplv@gmail.com' soft='87' />
            <User photo={userPhoto} name='Игнатюк Александр' age='18 лет' phone='+79215435242' email=' odvdplvdplv@gmail.com' soft='87' />
            <User photo={userPhoto} name='Игнатюк Александр' age='18 лет' phone='+79215435242' email=' odvdplvdplv@gmail.com' soft='87' />
        </div>
    )
}

export default Users