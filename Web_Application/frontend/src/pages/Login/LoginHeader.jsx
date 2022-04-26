import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';

import { makeStyles } from '@mui/styles';
import MenuItem from '@mui/material/MenuItem';
import Menu from '@mui/material/Menu';

import { Button } from '@mui/material';
import { Link } from 'react-router-dom';

import { useTheme } from '@mui/material/styles';
import useMediaQuery from '@mui/material/useMediaQuery';

const useStyles = makeStyles({
  root: {
    flexGrow: 1,
  },
});

export default function LoginHeader() {
  const classes = useStyles();
  const theme = useTheme();
  const [anchorEl, setAnchorEl] = React.useState(null);
  const isMobile = useMediaQuery(theme.breakpoints.down("sm"));

  const handleMenu = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <Box className={classes.root}>
      <AppBar position="static">
        <Toolbar>

          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Smart Tourist
          </Typography>

          {isMobile ? (
            <div>
              <IconButton
                size="large"
                edge="start"
                color="inherit"
                aria-label="menu"
                onClick={handleMenu}
                sx={{ mr: 2 }}
              >
              <MenuIcon />
              </IconButton>
              <Menu
                id="menu-appbar"
                anchorEl={anchorEl}
                anchorOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                keepMounted
                transformOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                open={Boolean(anchorEl)}
                onClose={handleClose}
              >
                <MenuItem onClick={handleClose}><Button variant="button" component={Link} to="/"> Home </Button></MenuItem>
                <MenuItem onClick={handleClose}><Button variant="button" component={Link} to="/login"> Login </Button></MenuItem>
                <MenuItem onClick={handleClose}><Button variant="button" component={Link} to="/signup"> Signup </Button></MenuItem>
              </Menu> 
            </div>
          ) : (
            <div>
              <Button variant="button" component={Link} to="/"> Home </Button>
              <Button variant="button" component={Link} to="/login"> Login </Button>
              <Button variant="button" component={Link} to="/signup"> Signup </Button>

            </div>
          )}
            
        </Toolbar>
      </AppBar>
    </Box>
  );
}
