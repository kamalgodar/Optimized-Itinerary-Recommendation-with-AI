import React from "react";
import useToken from "../useToken";
import Test0 from "./Home";
import Test2 from "./HomeA";

export default function Homecheck(){
    const { token, setToken } = useToken();
  
    if(!token) {
      return <Test0/>
    }
    else{
        return <Test2/>
    }
}
