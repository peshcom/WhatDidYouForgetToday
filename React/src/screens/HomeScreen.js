import React, {useEffect, useState} from 'react'
import axios from "axios";
import {Navigate} from "react-router-dom";


function HomeScreen() {
    let [posts, setPosts] = useState([])
    const getPosts = async () => {
        return await axios
            .get(
                "http://localhost:8000/v1/posts/",
                {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('access_token')
                    }
                }
            )
            .then((response) => {
                setPosts(response.data)
            })
            .catch((error) => {
                console.log(error.message);
            });
    }
    useEffect(
        async () => {
            return await getPosts();
        }, []
    )

    const removeElem = async (post_id) => {
        return await axios
            .delete(
                "http://localhost:8000/v1/posts/",
                {
                    data: {
                        post_id: post_id,
                    },
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('access_token'),
                    }
                },
            )
            .then((response) => {
                // request post again
                return getPosts();
            })
            .catch((error) => {
                console.log(error.message);
            });
    }
    const postList = posts.map(
        post => <div className="card mb-3">
            <div className="card-body">
                <div className="d-flex justify-content-between">
                    <div>{post.text}</div>
                    <div>
                        <button className="btn btn-sm btn-danger" onClick={() => removeElem(post.id)}>&#10008;</button>
                    </div>
                </div>
            </div>
        </div>
    )

    let [text, setText] = useState("")
    const submitHandler = async (e) => {
        e.preventDefault()
        return await axios
            .post(
                "http://localhost:8000/v1/posts/",
                {
                    text: text,
                },
                {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('access_token')
                    }
                }
            )
            .then((response) => {
                // clean field
                setText("");

                // request post again
                return getPosts();
            })
            .catch(
                (error) => {
                    console.log(error.message);
                }
            );
    }
    const createNew = <div className="card mb-3">
        <form onSubmit={submitHandler}>
            <div className="input-group">
                <input type="text" className="form-control" placeholder="Enter new message" value={text}
                       onChange={(event) => setText(event.target.value)} required={true}/>
                <button className="btn btn-outline-success" type="submit">Post!</button>
            </div>
        </form>
    </div>


    return (
        <div className="card w-50">
            {(() => {
                if (!localStorage.getItem('access_token')) {
                    return <Navigate to={'/login'}/>
                }
            })()}
            <div className="card-body">
                <h1>Home</h1>
                {createNew}
                {
                    !posts ? "posts not found" : postList
                }
            </div>
        </div>
    )
}

export default HomeScreen
