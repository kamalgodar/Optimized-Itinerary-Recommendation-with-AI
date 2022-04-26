import React from "react";
import Homecheck from "./Homecheck";

function Logout(){
    sessionStorage.clear();

return(
    <Homecheck/>
)
}
export default Logout;