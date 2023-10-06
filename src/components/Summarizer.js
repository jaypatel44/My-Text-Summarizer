import React, { useState } from 'react'

const Summarizer = (props) => {
    const [state, setState] = useState([{}]);
    const [text, setText] = useState("");

    const handleUpClick = async (e) => {
        e.preventDefault();
        const textr = { text };
        console.log(state)
        const response = await fetch("http://127.0.0.1:8000/analyze", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(textr)
        });
        if (response.ok) {
            console.log("It worked....")
        }
        setState(await response.json())
        console.log(state)

    }

    const handleUpperClick = (e) => {
        e.preventDefault();
        let newText = text.toUpperCase();
        setText(newText);
    }
    const handleLoClick = (e) => {
        e.preventDefault();
        let newText = text.toLowerCase();
        setText(newText);
    }
    const handeCopy = (e) => {
        e.preventDefault();
        var text = document.getElementById("myBox");
        text.select();
        navigator.clipboard.writeText(text.value);
    }
    const handleExtraSpaces = (e) => {
        e.preventDefault();
        let newText = text.split(/[ ]+/);
        setText(newText.join(" "));
    }


    const handleOnChange = (event) => {
        setText(event.target.value);
    }

    return (
        <>
            <div className='container'>
                <h1>Enter your text to summarize...</h1>
                <form>
                    <div className="mb-3" >
                        <textarea className="form-control" placeholder='Enter text here' value={text} onChange={handleOnChange} rows="8" id="myBox" style={{ backgroundColor: props.mode === 'dark' ? '#050926' : 'white', color: props.mode === 'dark' ? 'white' : 'black' }}></textarea>

                    </div>
                    <button type='submit' className='btn btn-primary mx-3 my-2' onClick={handleUpClick}>Get Your Summary</button>
                    <div>
                        <button className='btn btn-primary mx-3 my-2' onClick={handleUpperClick}>Convert to Uppercase</button>
                        <button className='btn btn-primary mx-3 my-2' onClick={handleLoClick}>Convert to Lowercase</button>
                        <button className='btn btn-primary mx-3 my-2' onClick={handeCopy}>Copy text</button>
                        <button className='btn btn-primary mx-3 my-2' onClick={handleExtraSpaces}>Remove Extra spaces</button>
                    </div>
                </form>

            </div>
            <div className="container my-3">
                <h2>Your Text Summary</h2>
                <p>No of words = {text.split(" ").filter((element) => { return element.length !== 0 }).length} and the no of Characters = {text.length}</p>
                <h2>Summary</h2>

                <p>{state.summary}</p>

            </div>

        </>
    )
}

export default Summarizer
