import React from "react";
import HomePage from "./pages/HomePage";
import Layout from "./pages/Layout";
import { BrowserRouter, Route, Routes } from "react-router";

const App = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Layout />}>
                    <Route index element={<HomePage />}></Route>
                </Route>
            </Routes>
        </BrowserRouter>
    );
};

export default App;
