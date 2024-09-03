// src/plugins/font-awesome.js

import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faStar, faBookmark } from "@fortawesome/free-solid-svg-icons";

library.add(faStar, faBookmark);

export default FontAwesomeIcon;
