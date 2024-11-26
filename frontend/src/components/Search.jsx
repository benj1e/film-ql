import React, { useEffect, useState, useTransition } from "react";
import axiosInstance from "../axiosConfig";
import ClipLoader from "react-spinners/ClipLoader"; // Import a spinner

const Search = ({ setResults, startTransition, setTotalResults }) => {
    const [query, setQuery] = useState("");
    // const [results, setResults] = useState([]);
    // const [isPending, startTransition] = useTransition();

    // const [totalResults, setTotalResults] = useState(0);
    const [debouncedQuery, setDebouncedQuery] = useState(query); // Debounced value

    // Debounce the query input to reduce the frequency of server requests
    useEffect(() => {
        const handler = setTimeout(() => {
            setDebouncedQuery(query);
        }, 700);

        return () => clearTimeout(handler);
    }, [query]);

    async function SearchDB(q) {
        axiosInstance
            .get("/movies/search", { params: { search: q } })
            .then((response) =>
                startTransition(() => {
                    console.log(response.statusText);
                    setTotalResults(response.data[0].totalResults || 0);
                    setResults(response.data[0].Search || []);
                })
            );
    }

    useEffect(() => {
        if (debouncedQuery) {
            SearchDB(debouncedQuery);
        }
    }, [debouncedQuery]);

    return (
        <>
            <div className="w-1/2 mx-auto my-4">
                <form className="mx-auto ">
                    <input
                        className="p-3 rounded w-full text-xl text-black border outline-none"
                        type="text"
                        name="search"
                        id="search"
                        placeholder="Search for a movie"
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                    />
                </form>
            </div>
        </>
    );
};

export default Search;
