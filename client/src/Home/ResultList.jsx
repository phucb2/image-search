import * as React from 'react';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import ImageListItemBar from '@mui/material/ImageListItemBar'

const exampleData = [
    {
        "name": "image_00001.jpg",
        "file_name": "../data/jpg/image_00001.jpg",
        "dist": 0.0
    },
    {
        "name": "image_00158.jpg",
        "file_name": "../data/jpg/image_00158.jpg",
        "dist": 8.062260671446696
    },
    {
        "name": "image_00073.jpg",
        "file_name": "../data/jpg/image_00073.jpg",
        "dist": 10.324985158559914
    },
    {
        "name": "image_00219.jpg",
        "file_name": "../data/jpg/image_00219.jpg",
        "dist": 10.804769901290944
    },
    {
        "name": "image_00214.jpg",
        "file_name": "../data/jpg/image_00214.jpg",
        "dist": 11.349800430834977
    },
    {
        "name": "image_00148.jpg",
        "file_name": "../data/jpg/image_00148.jpg",
        "dist": 11.482580494636027
    },
    {
        "name": "image_00049.jpg",
        "file_name": "../data/jpg/image_00049.jpg",
        "dist": 11.551506390470749
    },
    {
        "name": "image_00024.jpg",
        "file_name": "../data/jpg/image_00024.jpg",
        "dist": 11.684773358758518
    }
]

const URL = "http://localhost:8000/example"

class MyApp extends  React.Component {
    constructor(props) {
        super(props);
        this.state = {
            items: [],
            isLoaded: false
        };
    }

    componentDidMount() {
        fetch(URL)
            .then((res) => res.json())
            .then((json) => {
                this.setState({
                    isLoaded: true,
                    items: json
                })
            })
    }

    render() {
        const { isLoaded, items } = this.state;
        if (!isLoaded) {
            return <p>Loading</p>
        }
        return (
            <div>
                <ResultList data={items} />
            </div>
        )
    }
}

function ResultList(props) {
    const myStyle = {
        width: "248px",
        height: "248px",
        objectFix: "contain"
    }
    const list = new Array(5).fill(0).map((_, i) => i + 1)
    const zeroPad = (num, places) => String(num).padStart(places, '0')

    const getImage = (index) => `jpg/image_${zeroPad(index, 5)}.jpg`
    return <ImageList sx={{ width: 500, height: 200 }} cols={5}>
            { props.data.map((item) => (
                <ImageListItem key={item.name}>
                    <img
                        src={"jpg/" + item.name}
                        alt="title"
                        loading="lazy"/>
                    <ImageListItemBar
                        title={item.name}
                        subtitle={<span>by: {item.dist}</span>}
                         />
                </ImageListItem>))}    
        </ImageList>
}

export default MyApp;