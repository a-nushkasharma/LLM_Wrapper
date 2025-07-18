contract Case1 {
    address public highestBidder;
    uint public highestBid;

    function bid() public payable {
        require(msg.value > highestBid, "Too low");
        if (highestBidder != address(0)) {
            payable(highestBidder).transfer(highestBid); // refund previous
        }
        highestBid = msg.value;
        highestBidder = msg.sender;
    }
}