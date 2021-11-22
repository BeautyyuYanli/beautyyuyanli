const usetube = require('usetube')
const fs = require('fs')
const id = process.argv.slice(2)
usetube.getPlaylistVideos(id).then(res => {
    fs.writeFile('./latest.json', JSON.stringify(res), err => {console.log(err)})
})