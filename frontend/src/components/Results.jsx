import React from "react";
import ClipLoader from "react-spinners/ClipLoader";
import MovieItem from "./MovieItem";

const Results = ({ results, isPending, totalResults }) => {
    if (isPending) {
        return <ClipLoader />;
    }
    console.log(results);
    return (
        <div className="grid grid-cols-4 gap-6">
            {results.map((result, index) => (
                // <li key={index}>{result.Title}</li>
                <MovieItem result={result} key={index} />
            ))}
        </div>
    );
};

export default Results;
