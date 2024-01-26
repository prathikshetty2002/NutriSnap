"use client";
import { useState } from "react";
import "./Header.css";

const Header = () => {
  const [isActive, setIsActive] = useState(false);

  function toggleActive() {
    setIsActive(!isActive);
  }

  return (
    <>
      <div className="text-gray-950 w-full p-4 md:p-6 flex justify-between items-center max-md:mt-4">
        <div className="flex md:mx-12 items-center gap-2">
          <a href="/" className="flex">
            <img
              src="/logo.png"
              alt=""
              height={30}
              width={30}
              className="mr-4"
            />
            <h1 className="md:block font-bold text-xl">Nutrisnap</h1>
          </a>
        </div>
        <ul className="hidden list-none gap-12 my-4 md:mx-12 text-md text-gray-800 md:flex items-center justify-between">
          <li>
            <a href="#Contact">Login</a>
          </li>
          <li>
            <a
              href="#Faq"
              className=" rounded-full px-4 py-2 -ml-4 text-gray-100 bg-black hover:bg-white hover:text-black transition duration-300 ease-in-out"
            >
              Register
            </a>
          </li>
        </ul>
        <div
          className={`menu-btn-1 md:hidden mx-6 z-20 ${
            isActive ? "active" : ""
          }`}
          onClick={toggleActive}
        >
          <span></span>
        </div>
      </div>
      {isActive && <HamBurger />}
    </>
  );
};

export default Header;

const HamBurger = () => {
  return (
    <>
      <div className="absolute mt-2 rounded-lg border border-gray-50/20 z-10 bg-gray-50 drop-shadow-2xl backdrop-filter backdrop-blur-[6px] w-[96%] p-2">
        <ul className="list-none gap-12 my-4 text-xs flex flex-col items-center justify-between">
          <li>
            <a href="#">Home</a>
          </li>
          <li>
            <a href="#">Contact</a>
          </li>
          <li>
            <a href="#">FAQs</a>
          </li>
        </ul>
      </div>
    </>
  );
};
