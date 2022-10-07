import { Link } from "react-router-dom";
import StandardImageList from "./demo";
import TitlebarImageList from "./demo2";
import MyApp from "./ResultList";

export default function HomePage() {
    return (
    <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/users">Users</Link>
            </li>
          </ul>
        </nav>
        Home page
        <MyApp />
    </div>
    )
}