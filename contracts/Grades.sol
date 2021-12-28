//SPDX-License-Identifier: MIT

pragma solidity >=0.6.0;
pragma experimental ABIEncoderV2;

import "@openzeppelin/contracts/access/Ownable.sol";

contract Grades is Ownable {
    // Teacher address
    address public teacher;
    //mapping
    mapping(bytes32 => uint256) public StudentGrades;
    //array
    string[] reviews;
    //events
    event reviewed_student(bytes32);
    event event_review(string);

    //Constructor
    constructor() {
        teacher = msg.sender;
    }

    // evaluate student
    function evaluate(string memory _studentId, uint256 _grade)
        public
        onlyOwner
        returns (uint256)
    {
        //student identification hash
        bytes32 hash_statudentId = keccak256(abi.encodePacked(_studentId));
        // hash => studen Id
        StudentGrades[hash_statudentId] = _grade;
        // emit event
        emit reviewed_student(hash_statudentId);

        uint256 final_grade = StudentGrades[0];
        return final_grade;
    }
}
