const express = require("express")
const bodyparser = require("body-parser")
const { apply } = require("body-parser")
const axios = require('axios')
const http = require("http")
const https = require("https")
const fetch = require("node-fetch");
const ytdl = require('ytdl-core');
const fs = require('fs');
const path = require('path');
require("dotenv").config()

app = express()
app.use(express.json())
app.use(express.urlencoded({extended:false}))
function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms);
    });

}
app.get("/apiDownload", (req,res) =>{
    var data = req.query.name
    async function search(typed){
        const url = `https://www.googleapis.com/youtube/v3/search?part=id&q=${typed}&key=${process.env.API_KEY}`
        const response = await fetch(url)
        const data = await response.json()
        var vid = `https://youtube.com/watch?v=${data.items[0].id.videoId}`
        const down  = ytdl(vid,{filter:'audioonly'})
        down.pipe(fs.createWriteStream(__dirname+`\\downloads\\${typed}.mp3`));
        var mp3Path = path.join(__dirname, `\\downloads\\${typed}.mp3`)
        await sleep(3000)
        return mp3Path
    }
    search(data).then((path)=>{
        const finish = async()=>{
        res.type("application/octet-stream");        
        res.download(path)
        await sleep(60000)
        fs.unlinkSync(path)  
        }
        finish()
    })

})

http.createServer(app).listen(8000)