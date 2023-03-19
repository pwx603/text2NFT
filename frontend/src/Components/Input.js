import {Box, Button, FormControl, FormControlLabel, FormLabel, Radio, RadioGroup, TextField} from "@mui/material";
import {useState} from "react";
import axios from "axios";
import LoadingButton from '@mui/lab/LoadingButton';

export default function Input() {

    const [prompt, setPrompt] = useState("");
    const [loading, setLoading] = useState(false)
    const [act1textList, setAct1TextList] = useState([])
    const [act1Selection, setAct1Selection] = useState(0)
    const [act1ImgList, setAct1ImgList] = useState([])

    return (
        <div>
            <div>
                <br/>
                <br/>
                <br/>
                <TextField id="outlined-basic" label="Prompt" variant="outlined" value={prompt} onChange={ e => setPrompt(e.target.value)}/>
                <br/>
                <br/>
                <LoadingButton variant="outlined" loading={loading} onClick={()=> handleClick(prompt, setLoading, setAct1TextList)}> Generate Story </LoadingButton>
            </div>
            <br/>
            <br/>
            <Box >
                {
                    !!act1textList.length &&
                    <FormControl>
                        <FormLabel id="demo-radio-buttons-group-label">Act 1</FormLabel>
                        <RadioGroup
                            aria-labelledby="demo-radio-buttons-group-label"
                            defaultValue={act1Selection}
                            name="radio-buttons-group"
                            onChange={(e)=> { setAct1Selection(e.target.value) }}
                        >
                            { act1textList.map((msg, index)=> {
                                return <FormControlLabel value={index} control={<Radio />} label={msg} key={index}/>
                            })
                            }
                        </RadioGroup>
                        <LoadingButton variant="outlined" loading={loading} onClick={()=> generateImg(act1textList[act1Selection], setLoading, setAct1ImgList)}> Generate Photo </LoadingButton>
                    </FormControl>
                }
            </Box>
            <br/>
            <div>
                { !!act1ImgList.length &&
                    act1ImgList.map((imgSrc)=> {
                        return <img src={`data:image/png;base64,${imgSrc}`}/>
                    })
                }
            </div>
        </div>

    );
  }

let handleClick = async (prompt, setLoading, setAct1TextList) => {
    setLoading(true)
    try {
        let result = await axios.post("http://127.0.0.1:5000/prompt", {
            prompt: prompt
        })
        let a1List = result.data.choices.map((choice)=> {
            return choice.message.content
        })
        setAct1TextList(a1List)
    } catch (e) {
        console.log("error", e)
    } finally {
        setLoading(false)
    }
}

let generateImg = async(prompt, setLoading, setAct1ImgList) => {
    setLoading(true)
    try {
        let result = await axios.post("http://127.0.0.1:5000/txt2Img", {
            prompt: prompt
        })
        setAct1ImgList(result.data.images)
    } catch (e) {
        console.log("error", e)
    } finally {
        setLoading(false)
    }
}