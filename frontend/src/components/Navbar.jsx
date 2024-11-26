import React from "react";
import { NavLink } from "react-router";

const Navbar = () => {
    const baseLinkClass =
        "text-orange-800 text-xl shadow-lg linear transition-all px-4 py-2 rounded hover:bg-orange-200";

    const link = baseLinkClass + " bg-slate-100";
    const activeLink = baseLinkClass + " ring-3 bg-orange-100";
    return (
        <nav className="text-orange-800 border-b-2 py-4 px-5 w-full flex justify-between">
            <h1 className="text-orange-800 text-5xl">FilmQL</h1>

            {/* Search */}

            {/* Links */}
            <ul className="flex items-center gap-3">
                <li className="ms-auto">
                    <NavLink
                        to={"/"}
                        className={(isActive) =>
                            isActive ? activeLink : link
                        }>
                        Home
                    </NavLink>
                </li>
                {/* <li>
                    <NavLink
                        to={"/"}
                        className={(isActive) =>
                            isActive ? activeLink : link
                        }>
                        Home
                    </NavLink>
                </li> */}
            </ul>
        </nav>
    );
};

export default Navbar;
