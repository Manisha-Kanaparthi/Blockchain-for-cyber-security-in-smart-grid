// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract energymeter {
  string[] _v;
  string[] _c;
  string[] _p;

  function insertData(string memory v, string memory c, string memory p) public {
    _v.push(v);
    _c.push(c);
    _p.push(p);
  }

  function viewData() public view returns(string[] memory,string[] memory,string[] memory) {
    return(_v,_c,_p);
  }
}
