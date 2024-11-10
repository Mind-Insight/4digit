import React from "react"
import './../styles/Users.css'
import titlePhoto from './../images/title_photo.svg'
import User from "./User"
import userPhoto from './../images/profile.png'
import video from './../videos/visit.mp4'
import video2 from './../videos/visit1.mp4'
import video3 from './../videos/visit2.mp4'
import video4 from './../videos/visit3.mp4'
import video5 from './../videos/visit4.mp4'
import { useState } from 'react'

function Users() {

    const [users, setUsers] = useState([
        { id: 1, photo: userPhoto, name: 'Игнатюк Александр', age: '18 лет', phone: '+79115435242', email: 'odvdplvdplv@gmail.com', soft: '87', hard: '100', video: video, type: 'INTJ-A' },
        { id: 2, photo: userPhoto, name: 'Москаленко Анна', age: '38 лет', phone: '+79454325242', email: 'topiouloi@gmail.com', soft: '13', hard: '12', video: video2, type: 'ENTJ-A' },
        { id: 3, photo: userPhoto, name: 'Мязик Александр', age: '58 лет', phone: '+79156863442', email: 'vasyapup@gmail.com', soft: '87', hard: '13', video: video3, type: 'ENTB-A' },
        { id: 4, photo: userPhoto, name: 'Аверчинков Тимофей', age: '11 лет', phone: '+79215435242', email: 'google@gmail.com', soft: '87', hard: '0', video: video4, type: 'INTJ-T' },
        { id: 5, photo: userPhoto, name: 'Морозов Никита', age: '12 лет', phone: '+79215435243', email: 'mail@gmail.com', soft: '87', hard: '12', video: video5, type: 'INTJ-T' }
      ]);
    
      const handleDeleteUser = (id) => {
        setUsers(users.filter(user => user.id !== id))
      }

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
            {users.map(user => (
            <User
                id={user.id}
                key={user.phone}
                photo={user.photo}
                name={user.name}
                age={user.age}
                phone={user.phone}
                email={user.email}
                soft={user.soft}
                hard={user.hard}
                video={user.video}
                type={user.type}
                onDelete={handleDeleteUser}
            />
            ))}
        </div>
    )
}

export default Users