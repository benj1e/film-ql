import React, { useState, useTransition } from "react";
import Search from "./Search";
import Results from "./Results";
const Main = () => {
    const [results, setResults] = useState([]);
    const [isPending, startTransition] = useTransition();

    const [totalResults, setTotalResults] = useState(0);
    return (
        <div className="border">
            <Search
                setResults={setResults}
                startTransition={startTransition}
                setTotalResults={setTotalResults}
            />
            <Results
                results={results}
                isPending={isPending}
                totalResults={totalResults}
            />
        </div>
    );
};

export default Main;
