import React from "react";

const MovieItem = ({ result }) => {
    return (
        <div className="flex flex-col h-30">
            <img
                src={result.Poster}
                className="aspect-auto"
                alt={result.Title + " Poster"}
            />
            <span className="text-2xl font-serif"> {result.Title} </span>
        </div>
    );
};

export default MovieItem;
